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
  <v-container>
    <v-alert v-model="notFound" transition="slide-y-transition" type="warning">Palavra Não Encontrada</v-alert>
    <v-alert v-model="error" transition="slide-y-transition" type="error">Vish...</v-alert>
    <v-card color="#ffa726">
      <v-card-title>Adicione sua Query</v-card-title>
      <v-card-subtitle>Digite abaixo</v-card-subtitle>
      
      <v-card-text>
        <div v-if="isInit">
        <v-divider></v-divider>
          <div class="row ma-5">
            <div class="col"><h4>{{ optimized }}</h4></div>
            <div class="col"><h4 v-for="e in exec" :key="e">{{ e }}</h4></div>
            
            <div class="col d-flex justify-end">
              <v-img contain max-height="400" max-width="400" :src="src"></v-img>
            </div>
          </div>
        </div>
        <v-divider></v-divider>
      </v-card-text>
      
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-dialog
          v-model="dialog"
          width="500"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              color="#7da453"
              dark
              v-bind="attrs"
              v-on="on"
              class="mb-3"
            >
              Adicionar Query!  
            </v-btn>
          </template>

          <v-card color="#ffa726">
            <v-card-title>Qual sua query?</v-card-title>
            <v-divider></v-divider>
            <v-card-text>
              <v-textarea v-model="query" placeholder="DIGITA AI!"></v-textarea >
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="#aed581" class="mb-2" @click="optimizeQuery">Otimizar!</v-btn>
            </v-card-actions>
          </v-card>
          
        </v-dialog>
        <v-spacer></v-spacer>
      </v-card-actions>

    </v-card>
  </v-container>
</template>

<script>
export default {
  name: "HelloWorld",

  data() {
    return {
      isInit: false,
      dialog: false,

      notFound: false,
      error: false,

      query: "",
      optimized: "",
      exec: "Sequência Indisponível",
      src: "404.png"
    };
  },
  // mounted() {
    
  // },
  methods: {
    
    optimizeQuery() {
      const misc = {
        method: "POST",
        headers: {
          'Accept': 'application/json',
          "Content-Type": "application/json",
        },
        body: JSON.stringify({"sql": this.query})
      }

      fetch("http://localhost:6789/optimize", misc)
      .then((response) => {
        return response.json();
      })
      .then((json) => {
        console.log(json)
        this.optimized = json.alg
        this.exec = json.exec.split("\n")

        this.isInit = true
        this.dialog = false
      });
    },

    hide_notFound() {
      window.setInterval(() => {
        this.notFound = false;
      }, 5000);
    },

    hide_error() {
      window.setInterval(() => {
        this.error = false;
      }, 5000);
    },
  },
  watch: {
    notFound() {
      this.hide_notFound();
    },
    error() {
      this.hide_error();
    },
  }
};
</script>
