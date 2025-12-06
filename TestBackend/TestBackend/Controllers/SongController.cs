using LiteDB;
using Microsoft.AspNetCore.Mvc;
using SongBackend.Entities;
using SongBackend.Models;
using System.Net.Mime;

namespace SongBackend.Controllers;

[ApiController]
[Route("api")]
public class SongController : ControllerBase
{
    private readonly ILiteDatabase _database;
    private readonly ILiteCollection<SongEntity> _songs;
    private readonly ILiteCollection<UserEntity> _users;
    private readonly ISongStorage _storageService;

    public SongController(ILiteDatabase database, ISongStorage storageService)
    {
        _database = database;
        _songs = _database.GetCollection<SongEntity>();
        _users = _database.GetCollection<UserEntity>();
        _storageService = storageService;
    }

    [HttpGet("ns")]
    public IActionResult GetNextSong()
    {
        if (!HttpContext.Request.Headers.TryGetValue("Id", out var userIds) || userIds.Count != 1 || !Guid.TryParse(userIds[0], out var userId))
            return BadRequest("Missing Id Header");

        if (_users.FindById(userId) is not { } user)
        {
            //create new user for first time
            user = new UserEntity
            {
                Id = userId,
            };
            _users.Insert(user);
        }

        //todo: compare songs
        var rand = new Random();
        
        var songs = _songs.FindAll().ToArray();

        var song = songs[rand.Next(0, songs.Length)];

        var stream = _database.FileStorage.OpenRead(song.File);

        HttpContext.Response.Headers["SongName"] = song.Name;
        HttpContext.Response.Headers["SongId"] = song.Id.ToString();

        return File(stream, MediaTypeNames.Application.Octet);
    }

    [HttpGet("rt")]
    public IActionResult GetSongThumbnail([FromQuery] int songId)  // Fixed typo: GetSontThumbnail → GetSongThumbnail
    {
        //todo: database impl
        Console.WriteLine($"Request for thumbnail for {songId}");  // Fixed typo: thubmnail → thumbnail
        var stream = System.IO.File.OpenRead("testThumbnail.png");

        return File(stream, MediaTypeNames.Application.Octet);
    }

    [HttpPost("rs")]
    public IActionResult RateSong([FromBody] RateRequest request)
    {
        if (!HttpContext.Request.Headers.TryGetValue("Id", out var userIds) || userIds.Count != 1 || !Guid.TryParse(userIds[0], out var userId))
            return BadRequest("Missing Id Header");

        if (_users.FindById(userId) is not { } user)
            return Unauthorized();

        //todo
        Console.WriteLine($"{user.Id} {(request.PositiveRating ? "likes" : "dislikes")} {request.SongId}");

        
         _storageService.RateSong(user.Id.ToString(), request.SongId, request.PositiveRating);
        return Ok();
    }

    
    [HttpGet("likedsongs/{userId}")]
    public ActionResult<List<LikedSong>> GetLikedSongs(string userId)
    {
        var likedSongs = _storageService.GetLikedSongs(userId);
        return Ok(likedSongs);
    }

    [HttpDelete("likedsongs/{userId}/{songId}")]
    public IActionResult RemoveLikedSong(string userId, int songId)
    {
         _storageService.RemoveLike(userId, songId);
        return Ok();
    }
} 