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
        
        public ActionResult PersistentXSSGuestbook()
        {
            return View("PersistentXSS_Guestbook");
        }

        public ActionResult LocalXSS()
        {
            return View("LocalXSS"); 
        }

        public ActionResult LoginParcours()
        {
            return View("\\LoginParcours\\LoginParcoursHome"); 
        }

        public ActionResult LoginParcoursLevel1()
        {
            return View("\\LoginParcours\\LoginParcoursLevel1"); 
        }

        public ActionResult LoginParcoursLevel2()
        {
            return View("\\LoginParcours\\LoginParcoursLevel2");
        }
        public ActionResult LoginParcoursLevel3()
        {
            return View("\\LoginParcours\\LoginParcoursLevel3");
        }
        public ActionResult LoginParcoursLevel4()
        {
            return View("\\LoginParcours\\LoginParcoursLevel4");
        }

        public ActionResult LoginParcoursLevel5()
        {
            return View("\\LoginParcours\\LoginParcoursLevel5");
        }

        public ActionResult LoginParcoursLevel6()
        {
            return View("\\LoginParcours\\LoginParcoursLevel6");
        }

    }

}
