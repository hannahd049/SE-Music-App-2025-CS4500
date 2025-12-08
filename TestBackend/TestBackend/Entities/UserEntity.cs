using LiteDB;

namespace SongBackend.Entities;

public record UserEntity
{
    public Guid Id { get; init; }

    public HashSet<RatedSong> LikedSongs { get; init; } = [];
    public HashSet<RatedSong> DislikedSongs { get; init; } = [];
}
