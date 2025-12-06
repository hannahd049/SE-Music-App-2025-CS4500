using LiteDB;
using SongBackend.Entities;
using SongBackend.Models;

var builder = WebApplication.CreateBuilder(args);

var db = new LiteDatabase(builder.Configuration.GetConnectionString("LiteDb"));


SetupSongs(builder.Configuration, db);

// Add services to the container.
builder.Services.AddControllers();

builder.Services.AddSingleton<ILiteDatabase>(db);
builder.Services.AddSingleton<ISongStorage, DatabaseSongStorage>();

if (builder.Environment.IsDevelopment())
{
    builder.Services.AddHttpLogging(options =>
    {
        options.RequestHeaders.Add("Id");
    });
}

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseHttpLogging();
}

app.UseAuthorization();
app.MapControllers();

await app.RunAsync();

static void SetupSongs(IConfiguration config, ILiteDatabase db)
{
    var songs = db.GetCollection<SongEntity>();
    var artists = db.GetCollection<ArtistEntity>();
    //Check for new songs to add to db
    var folder = config["MusicFolder"]
        ?? throw new InvalidDataException("Missing MusicFolder in configuration");

    if (!Directory.Exists(folder))
        Directory.CreateDirectory(folder);

    var files = Directory.GetFiles(folder, "*.mp3");

    if (files.Length == 0)
        throw new InvalidOperationException($"No mp3 files found in {Path.GetFullPath(folder)}");

    foreach (var file in files)
    {
        var fileName = Path.GetFileName(file);
        if (songs.FindOne(x => x.File == fileName) != null)
            continue; //song already in db

        //add song to db
        var songName = GetCliInput<string>($"Enter the name of the song for {file}: ");

        ArtistEntity? artist;
        do
        {
            var artistName = GetCliInput<string>($"Enter the name of the artist for {file}: ");
            artist = artists.FindOne(x => x.Name == artistName);
            if (artist == null)
            {
                var createNew = GetCliInput<bool>($"No artist found named '{artistName}'. Create new artist? ");

                if (createNew)
                {
                    artist = new ArtistEntity
                    {
                        Id = ObjectId.NewObjectId(),
                        Name = artistName,
                    };
                    artists.Insert(artist);
                }
            }
        } while (artist == null);
        var genre = GetCliInputEnum<Genres>("Enter Song Genre: ");

        var song = new SongEntity
        {
            Artist = artist,
            Genre = genre,
            File = fileName,
            Name = songName,
        };

        songs.Insert(song);

        using var fs = File.OpenRead(file);
        db.FileStorage.Upload(fileName, "song.mp3", fs);

        Console.WriteLine($"Added: {song}");
    }
    db.Checkpoint();
}

static T GetCliInput<T>(string prompt) where T : IParsable<T>
{
    for(;;)
    {
        Console.Write(prompt);
        var str = Console.ReadLine();

        if (T.TryParse(str, null, out var value))
            return value;

        Console.WriteLine("Failed to parse input, try again");
    }
}
static T GetCliInputEnum<T>(string prompt) where T : struct
{
    for (; ; )
    {
        Console.Write(prompt);
        var str = Console.ReadLine();

        if (Enum.TryParse<T>(str, out var value))
            return value;

        Console.WriteLine("Failed to parse input, try again");
        Console.WriteLine("Valid Options:");
        foreach (var val in Enum.GetNames(typeof(T)))
            Console.WriteLine(val);
    }
}