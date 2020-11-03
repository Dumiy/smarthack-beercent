import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';

@Injectable({
    providedIn: 'root'
})
export class LoaderService {
    private _isDisplayed: BehaviorSubject<boolean> = new BehaviorSubject<boolean>(false);

    get isActionPending(): Observable<boolean> {
        return this._isDisplayed.asObservable();
    }

    get value(): boolean {
        return this._isDisplayed.value;
    }

    showLoader(): void {
        // TODO_AC: Temporary solution for the ExpressionChangedAfterItHasBeenCheckedError
        // Can be removed after LoaderService is added to all parts of the app
        setTimeout(() => this._isDisplayed.next(true), 0);
    }

    hideLoader(): void {
        setTimeout(() => this._isDisplayed.next(false), 0);
    }
}