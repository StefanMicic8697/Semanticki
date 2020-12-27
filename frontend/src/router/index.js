import Vue from 'vue'
import VueRouter from 'vue-router'

import Kurs from '../components/Kurs.vue'
import NastavniMaterijal from '../components/NastavniMaterijal.vue'
import ObrazovniCilj from '../components/ObrazovniCilj.vue'
import StudijskiProgram from '../components/StudijskiProgram.vue'
import Pretraga from '../components/Pretraga.vue'
import SPARQL from '../components/SPARQL.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/kurs',
    name: 'Kurs',
    component: Kurs
  },
  {
    path: '/nastavni-materijal',
    name: 'NastavniMaterijal',
    component: NastavniMaterijal
  },
  {
    path: '/obrazovni-cilj',
    name: 'ObrazovniCilj',
    component: ObrazovniCilj
  },
  {
    path: '/studijski-program',
    name: 'StudijskiProgram',
    component: StudijskiProgram
  },
  {
    path: '/pretraga',
    name: 'Pretraga',
    component: Pretraga
  },
  {
    path: '/sparql',
    name: 'SPARQL',
    component: SPARQL
  },
]

const router = new VueRouter({
  routes
})

export default router
