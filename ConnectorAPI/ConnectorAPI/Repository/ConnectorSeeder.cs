using ConnectorAPI.Models;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Identity;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace ConnectorAPI.Repository
{
    public class ConnectorSeeder
    {
        private readonly ConnectorContext _ctx;
        private readonly IWebHostEnvironment _hosting;
        private readonly UserManager<User> _userManager;

        public ConnectorSeeder(ConnectorContext ctx, IWebHostEnvironment hosting, UserManager<User> userManager)
        {
            _ctx = ctx;
            _hosting = hosting;
            _userManager = userManager;
        }

        public async Task SeedAsync()
        {
            _ctx.Database.EnsureCreated();

            User user = await _userManager.FindByEmailAsync("beercent@gmail.com");
            if (user == null)
            {
                user = new User()
                {
                    UserName = "BeerCent",
                    Email = "beercent@gmail.com",
                    FirstName = "Beer",
                    LastName = "Cent"
                };

                var result = await _userManager.CreateAsync(user, "Password01!");
                if (result != IdentityResult.Success)
                {
                    throw new InvalidOperationException("Could not create new user in seeder!");
                }
            }
        }
    }
}
