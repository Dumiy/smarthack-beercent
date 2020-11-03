import { Component, OnInit } from '@angular/core';
import { TestService, AuthenticationService, ProductService } from '../../../../api/services';
import { IProduct } from 'src/app/modules/product/models';

@Component({
  selector: 'app-find',
  templateUrl: './find.component.html',
  styleUrls: ['./find.component.scss']
})
export class FindComponent implements OnInit {
  res;
  productList: IProduct[] = []
  isLoading = false;
  productListMock: IProduct[]= [
    {
      name: 'Laptop GL552',
      url: 'https://emag.ro',
      score: 4.8
    },
    {
      name: 'Samsung A7 2018',
      url: 'https://emag.ro',
      score: 4.1
    },
    {
      name: 'Samsung Galaxy Buds',
      url: 'https://emag.ro',
      score: 3.2
    },
    {
      name: 'Allview Naspa',
      url: 'https://emag.ro',
      score: 1.3
    }
  ];
  constructor(public testApiService: TestService, private productService: ProductService, public authService: AuthenticationService) { }

  ngOnInit(): void {
  }

  getProductList(object): void {
    this.isLoading = true;

    this.productService.getProductsByKeys(object).subscribe(
      (result) => {
        let obj = JSON.parse(result);
        if(!obj) {
          this.productList = this.productListMock;
          return;
        }
        let productsSet: Set<IProduct> = new Set<IProduct>();
        for(let prop in obj) {
          productsSet.add({
            name: prop,
            score: (obj[prop] as number).toFixed(2),
            url: 'www.compari.ro'
          })
        }
        this.productList = Array.from(productsSet).sort((p1, p2) => {
          return p1.score > p2.score
          ? -1 : p1.score < p2.score
          ? 1 :0;
        });
      },
      (error) => console.log(error),
      () => this.isLoading = false
    );
    // setTimeout(() => {
    //   this.isLoading = false;
    //   this.productList = this.productListMock;
    // }, 3000);
  }

  clearData(): void {
    this.productList = [];
  }
}
