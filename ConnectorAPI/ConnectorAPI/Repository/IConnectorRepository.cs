using ConnectorAPI.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace ConnectorAPI.Repository
{
    public interface IConnectorRepository
    {
        IEnumerable<User> GetAllUsers();
        User GetUserById(string id);
        bool UpdateUser(User user);
        bool DeleteUser(string id);
        bool SaveAll();
    }
}
