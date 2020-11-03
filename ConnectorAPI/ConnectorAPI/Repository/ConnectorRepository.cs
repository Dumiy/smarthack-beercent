using ConnectorAPI.Models;
using Microsoft.EntityFrameworkCore;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace ConnectorAPI.Repository
{
    public class ConnectorRepository : IConnectorRepository
    {
        private readonly ConnectorContext _ctx;

        public ConnectorRepository(ConnectorContext ctx)
        {
            _ctx = ctx;
        }

        public IEnumerable<User> GetAllUsers()
        {
            return _ctx.Users
                .OrderBy(p => p.UserName)
                .ToList();
        }

        public User GetUserById(string id)
        {
            return _ctx.Users
                .FirstOrDefault(u => u.Id.Equals(id));
        }

        public bool UpdateUser(User user)
        {
            try
            {
                _ctx.Update(user);
                return true;
            }
            catch (DbUpdateException)
            {
                return false;
                throw;
            }
        }

        public bool DeleteUser(string id)
        {
            try
            {
                User user = this.GetUserById(id);
                _ctx.Remove(user);
                return true;
            }
            catch (DbUpdateException)
            {
                return false;
                throw;
            }
        }

        public bool SaveAll()
        {
            return _ctx.SaveChanges() > 0;
        }
    }
}
