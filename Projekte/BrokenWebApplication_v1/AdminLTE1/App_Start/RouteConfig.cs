﻿using System.Web.Mvc;
using System.Web.Routing;

namespace AdminLTE1
{
    public class RouteConfig
    {
        public static void RegisterRoutes(RouteCollection routes)
        {
            routes.IgnoreRoute("{resource}.axd/{*pathInfo}");

            routes.MapRoute(
                "SecurityWorkbench",                                                        // Route name
                "SecurityWorkbench/",                                                       // URL with parameters
                new { controller = "Home", action = "Index", id = UrlParameter.Optional }
                );

            routes.MapRoute(
                name: "Default",
                url: "{controller}/{action}/{id}",
                defaults: new { controller = "Home", action = "Index", id = UrlParameter.Optional }
                );
        }
    }
}
