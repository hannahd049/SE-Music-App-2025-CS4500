using System.Text.Json.Serialization;

namespace SongBackend.Models;

public class RateRequest
{
    [JsonPropertyName("songId")]
    public int SongId { get; set; }

    [JsonPropertyName("positive")]
    public bool PositiveRating { get; set; }
}
