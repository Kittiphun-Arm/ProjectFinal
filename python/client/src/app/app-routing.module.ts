import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { MapComponent } from './components/map/map.component';
import { MenuComponent } from './components/menu/menu.component';

const routes: Routes = [
  {path: 'home' ,component:HomeComponent},
  {path: 'map' ,component:MapComponent},
  {path: 'menu', component:MenuComponent},
  {path: '',
    redirectTo: 'home',
    pathMatch: 'full'
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
