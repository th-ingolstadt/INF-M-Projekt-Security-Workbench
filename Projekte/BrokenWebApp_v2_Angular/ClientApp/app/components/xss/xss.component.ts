import { Component } from '@angular/core';

@Component({
    selector: 'xss',
    templateUrl: './xss.component.html'
})
export class XSSComponent {
    public currentCount = 0;

    public incrementCounter() {
        this.currentCount++;
    }
}
