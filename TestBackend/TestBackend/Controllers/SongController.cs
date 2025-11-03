using Microsoft.AspNetCore.Mvc;
using System.Net.Mime;
using TestBackend.Models;

namespace TestBackend.Controllers;

[ApiController]
[Route("api")]
public class SongController : ControllerBase
{

    [HttpGet("ns")]
    public IActionResult GetNextSong()
    {
        var stream = System.IO.File.OpenRead("test.mp3");

        HttpContext.Response.Headers["SongName"] = "TestSong";
        HttpContext.Response.Headers["SongId"] = "1234";

        return File(stream, MediaTypeNames.Application.Octet);
    }

    [HttpGet("rt")]
    public IActionResult GetSontThumbnail([FromQuery] int songId)
    {
        //todo: database impl
        Console.WriteLine($"Request for thubmnail for {songId}");
        var stream = System.IO.File.OpenRead("testThumbnail.png");

        return File(stream, MediaTypeNames.Application.Octet);
    }

    [HttpPost("rs")]
    public IActionResult RateSong([FromBody] RateRequest request)
    {
        //todo:

        Console.WriteLine($"{request.UserId} {(request.PositiveRating ? "likes" : "dislikes")} {request.SongId}");

        return Ok();
    }
}
