using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Nancy.Json;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

namespace ConnectorAPI.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class SearchEngineController : ControllerBase
    {
        [HttpGet]
        public JsonResult Get()
        {
            var str = "Salut Marcu, in container este ora: " + DateTime.Now;
            return new JsonResult(str);
        }
    }
}
