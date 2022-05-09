<template>
  <!-- 
  Colors:
  - P   = #aed581   (D)
  - PC  = #e1ffb1   (D)
  - PD  = #7da453   (l)
  - S   = #ffa726   (l)
  - SC  = #ffd95b   (l)
  - SD  = #c77800   (l)
  -->
  <v-app>
    <v-app-bar
      app
      color="#aed581"
    >
      <div class="d-flex align-center text-h5">
        <v-icon>mdi-graphql</v-icon>
        Graphinator
      </div>

      <v-spacer></v-spacer>

      <v-btn
        href="https://github.com/GhosTheKaos3150/PBD-indexhash-app"
        target="_blank"
        text
      >
        <span class="mr-2">GITHUB</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    //
  }),
};
</script>
