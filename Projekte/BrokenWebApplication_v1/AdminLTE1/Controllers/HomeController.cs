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

        public ActionResult SessionManagementAufgabe1()
        {
            return View("SessionManagementAufgabe1");
        }

        public ActionResult SessionManagementAufgabe2()
        {
            return View("SessionManagementAufgabe2");
        }

        public ActionResult SessionManagementAufgabe3()
        {
            return View("SessionManagementAufgabe3");
        }


        public ActionResult PersistentXSSGuestbook()
        {
            return View("PersistentXSS_Guestbook");
        }

    }

}





    

