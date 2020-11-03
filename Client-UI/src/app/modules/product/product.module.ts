import { NgModule } from '@angular/core';
import { ProductCardComponent } from './components';
import { SharedModule } from '../shared/shared.module';
import { ProductListComponent } from './components/product-list/product-list.component';

@NgModule({
    declarations: [ProductCardComponent, ProductListComponent],
    imports: [
        SharedModule
    ],
    exports: [ProductListComponent],
    providers: [],
})
export class ProductModule {}
