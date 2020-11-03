import { Component, OnInit, Input } from '@angular/core';
import { IProduct } from '../../models/';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.scss']
})
export class ProductListComponent implements OnInit {

  @Input()
  productList: IProduct[] = [];
  constructor() { }

  ngOnInit(): void {
  }

}
