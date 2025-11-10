using TestBackend.Models;  // THIS LINE MUST BE AT THE TOP

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddControllers();
builder.Services.AddSingleton<SongStorage, MemorySongStorage>();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
}

app.UseAuthorization();
app.MapControllers();

await app.RunAsync();
