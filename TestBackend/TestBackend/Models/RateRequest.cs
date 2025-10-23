using System.Text.Json.Serialization;

namespace TestBackend.Models;

public class RateRequest
{
    [JsonPropertyName("songId")]
    public int SongId { get; set; }

    [JsonPropertyName("positive")]
    public bool PositiveRating { get; set; }

    [JsonPropertyName("userId")]
    public string UserId { get; set; } = string.Empty;
}
