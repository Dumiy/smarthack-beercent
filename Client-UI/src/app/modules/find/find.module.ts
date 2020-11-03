import { NgModule } from '@angular/core';
import { FindComponent } from './components';
import { SharedModule } from '../shared/shared.module';
import { ProductModule } from '../product/product.module';
import { SearchModule } from '../search/search.module';

@NgModule({
    declarations: [FindComponent],
    imports: [
        SharedModule,
        ProductModule,
        SearchModule
    ],
    exports: [FindComponent],
    providers: [],
})
export class FindModule {}
