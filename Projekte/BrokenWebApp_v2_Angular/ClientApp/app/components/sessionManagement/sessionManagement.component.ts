import { Component } from '@angular/core';

@Component({
    selector: 'sessionManagement',
    templateUrl: './sessionManagement.component.html'
})
export class SessionManagementComponent {
    public currentCount = 0;

    public incrementCounter() {
        this.currentCount++;
    }
}
