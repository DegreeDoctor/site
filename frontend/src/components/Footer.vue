<template>
  <q-layout view="hHh LpR fFf">

    <q-page-container>
      <router-view />
    </q-page-container>

    <q-footer elevated class="bg-grey-8 text-white">
      <q-toolbar>
        <q-toolbar-title class="text-center">
          <q-icon name="fa-brands fa-github" />
          
        </q-toolbar-title>
      </q-toolbar>
    </q-footer>

  </q-layout>
</template>