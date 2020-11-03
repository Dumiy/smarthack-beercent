import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-product-card',
  templateUrl: './product-card.component.html',
  styleUrls: ['./product-card.component.scss']
})
export class ProductCardComponent implements OnInit {
  @Input()
  image: any;
  @Input()
  score: number;
  @Input()
  name: string
  @Input()
  url = "https://emag.ro";
  constructor() { }

  ngOnInit(): void {
  }

  getBubbleColorScore(): string {
    return this.score <= 3.5
    ? 'red'
    : this.score > 3.5 && this.score < 7
    ? 'yellow'
    : 'green'
  }

  goToLink(): void {
    const keywords = this.name.split(' ').join('+');
    window.open(`https://www.price.ro/index.php?action=q&text=${keywords}&submit=Cauta`, '_blank');
  }
}
