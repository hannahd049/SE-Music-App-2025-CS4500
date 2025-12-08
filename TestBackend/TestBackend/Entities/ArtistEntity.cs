using LiteDB;

namespace SongBackend.Entities;

public record ArtistEntity
{
    public required ObjectId Id { get; init; }
    public required string Name { get; init; }
}
