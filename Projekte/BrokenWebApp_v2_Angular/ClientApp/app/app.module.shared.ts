import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { RouterModule } from '@angular/router';

import { AppComponent } from './components/app/app.component';
import { NavMenuComponent } from './components/navmenu/navmenu.component';
import { HomeComponent } from './components/home/home.component';
import { SessionManagementComponent } from './components/sessionManagement/sessionManagement.component';
import { XSSComponent } from './components/xss/xss.component'; 

@NgModule({
    declarations: [
        AppComponent,
        NavMenuComponent,
        SessionManagementComponent,
        HomeComponent,
        XSSComponent
    ],
    imports: [
        CommonModule,
        HttpModule,
        FormsModule,
        RouterModule.forRoot([
            { path: '', redirectTo: 'home', pathMatch: 'full' },
            { path: 'home', component: HomeComponent },
            { path: 'xss', component: XSSComponent },
            { path: 'sessionManagement', component: SessionManagementComponent },
            { path: '**', redirectTo: 'home' }
        ])
    ]
})
export class AppModuleShared {
}
