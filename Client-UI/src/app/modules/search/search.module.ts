import { NgModule } from '@angular/core';
import { SearchComponent } from './components';
import { SharedModule } from '../shared/shared.module';
import { ProductModule } from '../product/product.module';

@NgModule({
    declarations: [SearchComponent],
    imports: [
        SharedModule,
        ProductModule
    ],
    exports: [SearchComponent],
    providers: [],
})
export class SearchModule {}
