import {
    HttpEvent,
    HttpHandler,
    HttpInterceptor,
    HttpRequest
  } from '@angular/common/http';
  import { Injectable } from '@angular/core';
  import { Router } from '@angular/router';
  import { Observable, of, throwError } from 'rxjs';
  import { catchError } from 'rxjs/operators';
  import { LoaderService } from './loader.service';

  @Injectable()
  export class ApiInterceptor implements HttpInterceptor {
    constructor(
      private router: Router,
      private loaderService: LoaderService
    ) { }

    intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
      const token: string = sessionStorage.getItem('currentUser') || localStorage.getItem('currentUser');
      // Apply the headers
      req = req.clone({
        setHeaders: {
          Authorization: token && `Bearer ${token}` || ''
        }
      });
      return next.handle(req).pipe(
        catchError((res: any) => {
          switch (res.status) {
            case 401:
            case 402:
            case 403: {
              this.loaderService.hideLoader();
              if (this.router.url === '/login') {
                return throwError(res);
              }
              return of(null);
            }
            default: {
              this.loaderService.hideLoader();
              return throwError(res);
            }
          }
        })
      );
    }
  }