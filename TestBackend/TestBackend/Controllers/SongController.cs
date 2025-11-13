using Microsoft.AspNetCore.Mvc;
using System.Net.Mime;
using TestBackend.Models;

namespace TestBackend.Controllers;

[ApiController]
[Route("api")]
public class SongController : ControllerBase
{
    private readonly SongStorage _storageService;

    public SongController(SongStorage storageService)
    {
        _storageService = storageService;
    }

    [HttpGet("ns")]
    public IActionResult GetNextSong()
    {
        var stream = System.IO.File.OpenRead("test.mp3");

        HttpContext.Response.Headers["SongName"] = "TestSong";
        HttpContext.Response.Headers["SongId"] = "1234";

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
        //todo
        Console.WriteLine($"{request.UserId} {(request.PositiveRating ? "likes" : "dislikes")} {request.SongId}");

        
         _storageService.RateSong(request.UserId, request.SongId, request.PositiveRating);
        return Ok();
    }

    
    [HttpGet("likedsongs/{userId}")]
    public ActionResult<List<LikedSong>> GetLikedSongs(string userId)
    {
        var likedSongs = await _storageService.GetLikedSongs(userId);
        return Ok(likedSongs);
    }

    [HttpDelete("likedsongs/{userId}/{songId}")]
    public IActionResult RemoveLikedSong(string userId, int songId)
    {
         _storageService.RemoveLike(userId, songId);
        return Ok();
    }
}