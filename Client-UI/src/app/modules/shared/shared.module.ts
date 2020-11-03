import { NgModule, forwardRef, Provider, ModuleWithProviders } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { MaterialModule } from './material.module';
import { ApiInterceptor, LoaderService } from './services';
import { SidenavComponent, ToolbarComponent } from './components';

export const API_INTERCEPTOR_PROVIDER: Provider = [
    {
      provide: HTTP_INTERCEPTORS,
      useExisting: forwardRef(() => ApiInterceptor),
      multi: true
    }
]

@NgModule({
    imports: [
        HttpClientModule,
        CommonModule,
        FormsModule,
        MaterialModule,
        RouterModule,
        ReactiveFormsModule
    ],
    declarations: [
        SidenavComponent,
        ToolbarComponent
    ],
    exports: [
        MaterialModule,
        HttpClientModule,
        CommonModule,
        FormsModule,
        RouterModule,
        ReactiveFormsModule,
        SidenavComponent,
        ToolbarComponent
    ],
    providers: [
        ApiInterceptor,
        LoaderService
    ]
})
export class SharedModule {}