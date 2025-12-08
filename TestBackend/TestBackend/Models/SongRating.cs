using LiteDB;
using SongBackend.Entities;

namespace SongBackend.Models;

public class SongRating
{
    public int SongId { get; set; }
    public string UserId { get; set; } = string.Empty;
    public bool Positive { get; set; }
    public DateTime RatedAt { get; set; } = DateTime.UtcNow;
}

public class LikedSong
{
    public int SongId { get; set; }
    public string SongName { get; set; } = string.Empty;
    public  DateTime LikedAt {get; set; }
}

public interface ISongStorage
{
    void RateSong(string userId, int songId, bool positive);
    List<LikedSong> GetLikedSongs(string userId); 
    void RemoveLike(string userId, int songId);
}
public class DatabaseSongStorage(ILiteDatabase db) : ISongStorage
{
    private readonly ILiteCollection<UserEntity> _users = db.GetCollection<UserEntity>().Include(x => x.LikedSongs).Include(x => x.DislikedSongs);
    private readonly ILiteCollection<SongEntity> _songs = db.GetCollection<SongEntity>();

    public List<LikedSong> GetLikedSongs(string userId)
    {
        if (!Guid.TryParse(userId, out var id) || _users.FindById(id) is not { } user)
            throw new InvalidOperationException($"Invalid user id: {userId}");

        return [.. user.LikedSongs.Select(x =>
        {
            if (_songs.FindById(x.SongId) is not { } song)
                throw new InvalidOperationException($"Unknown song id: {x.SongId}");
            return new LikedSong
            {
                SongId = song.Id,
                SongName = song.Name,
                LikedAt = x.RatedTime,
            };
        })];
    }

    public void RateSong(string userId, int songId, bool positive)
    {
        if (!Guid.TryParse(userId, out var id) || _users.FindById(id) is not { } user)
            throw new InvalidOperationException($"Invalid user id: {userId}");

        if (_songs.FindById(songId) is not { })
            throw new InvalidOperationException($"Unknown song id: {songId}");

        var rating = new RatedSong
        {
            SongId = songId
        };

        //remove old rating
        user.LikedSongs.Remove(rating);
        user.DislikedSongs.Remove(rating);

        if (positive)
            user.LikedSongs.Add(rating);
        else
            user.DislikedSongs.Add(rating);

        _users.Update(user);
    }

    public void RemoveLike(string userId, int songId)
    {
        if (!Guid.TryParse(userId, out var id) || _users.FindById(id) is not { } user)
            throw new InvalidOperationException($"Invalid user id: {userId}");

        if (_songs.FindById(songId) is not { })
            throw new InvalidOperationException($"Unknown song id: {songId}");

        var rating = new RatedSong
        {
            SongId = songId
        };

        user.LikedSongs.Remove(rating);
        _users.Update(user);
    }
}

public class MemorySongStorage : ISongStorage
{
    private readonly List<SongRating> _ratings = new();
    private readonly Dictionary<int, string> _songNames = new();

    public MemorySongStorage()
    {
        _songNames[1234] = "TestSong";
    }

    public void RateSong(string userId, int songId, bool positive)
    {
       
        

        _ratings.RemoveAll(r => r.UserId == userId && r.SongId == songId);  
        
        if(positive)
        {
            _ratings.Add(new SongRating
            {
                UserId = userId,
                SongId = songId,
                Positive = positive,
                RatedAt = DateTime.UtcNow
            });
        }
    }

    public List<LikedSong> GetLikedSongs(string userId)
    {   
        

        var likedSongs = _ratings
            .Where(r => r.UserId == userId && r.Positive)
            .OrderByDescending(r => r.RatedAt)
            .Select(r => new LikedSong
            {
                SongId = r.SongId,
                SongName = _songNames.GetValueOrDefault(r.SongId, "Unknown Song"),  
                LikedAt = r.RatedAt
            })
            .ToList();

        return likedSongs;
    }

    public void RemoveLike(string userId, int songId)
    {

        _ratings.RemoveAll(r => r.UserId == userId && r.SongId == songId);
    }
}
 