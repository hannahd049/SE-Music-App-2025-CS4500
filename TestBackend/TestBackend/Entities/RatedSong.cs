using LiteDB;

namespace SongBackend.Entities;

public class RatedSong : IEquatable<RatedSong>
{
    public int SongId { get; set; }
    public DateTime RatedTime { get; set; } = DateTime.UtcNow;

    public bool Equals(RatedSong? other) => other != null && other.SongId == SongId;

    public override bool Equals(object? obj) => Equals(obj as RatedSong);

    public override int GetHashCode() => SongId;
}
