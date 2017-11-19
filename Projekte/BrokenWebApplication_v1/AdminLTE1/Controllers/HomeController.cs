using System.Web.Mvc;

namespace AdminLTE1.Controllers
{
    public class HomeController : Controller
    {
        public ActionResult Index()
        {
            return View();
        }

        public ActionResult AnotherLink()
        {
            return View("Index");
        }

        public ActionResult TestLink()
        {
            return View("Test");
        }

        public ActionResult SessionManagementLink()
        {
            return View("SessionManagement"); 
        }

        public ActionResult BufferOverflow()
        {
            return View("BufferOverflow");
        }

        public ActionResult BufferOverflow_FirstExample()
        {
            return View("BufferOverflow_FirstExample");
        }

        public ActionResult BufferOverflow_SecondExample()
        {
            return View("BufferOverflow_SecondExample");
        }
    }

}
