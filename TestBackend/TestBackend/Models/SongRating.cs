namespace TestBackend.Models;

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

public interface SongStorage
{
    void RateSong(string userId, int songId, bool positive);
    List<LikedSong> GetLikedSongs(string userId); 
    void RemoveLike(string userId, int songId);
}

public class MemorySongStorage : SongStorage
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
 