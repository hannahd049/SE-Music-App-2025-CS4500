using LiteDB;

namespace SongBackend.Entities;

public record SongEntity
{
    public int Id { get; init; }
    public Genres Genre { get; init; }
    public required string File { get; init; }
    public required string Name { get; init; }
    [BsonRef]
    public required ArtistEntity Artist { get; init; } = null!;
}
