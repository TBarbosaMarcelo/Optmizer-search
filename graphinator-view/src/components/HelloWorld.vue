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
            <div class="col">TESTE1</div>
            
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
              <v-text-field placeholder="DIGITA AI!"></v-text-field>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="#aed581" class="mb-2">Otimizar!</v-btn>
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
      isInit: true,

      notFound: false,
      error: false,

      query: "",
      src: "404.png"
    };
  },
  mounted() {
    fetch("http://localhost:3150/hash/initqm")
      .then((response) => {
        return response.json();
      })
      .then((json) => {
        console.log(json)
        this.isInit = json.init;
      });
  },
  methods: {
    loadFile() {
      this.fileLoading = true

      if (this.textFile != null) {
        var reader = new FileReader();

        reader.onload = () => {
          this.text = reader.result;
          this.fileLoading = false;
        };
        reader.readAsText(this.textFile);
      } else {
        this.fileLoading = false; 
      }
    },
    async initHash() {
      console.log(this.t_bucket, this.t_pag)
      console.log(typeof this.t_bucket, typeof this.t_pag)

      await fetch("http://localhost:3150/hash", {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          text: this.text,
          t_bucket: parseInt(this.t_bucket),
          t_pag: parseInt(this.t_pag),
        }),
      });

      fetch("http://localhost:3150/hash/initqm")
      .then((response) => {
        return response.json();
      })
      .then((json) => {
        console.log(json)
        this.isInit = json.init;
      });
    },

    async pesquisarHash() {
      this.isResponseAvailable = false;

      await fetch(`http://localhost:3150/hash/search/${this.searchWord}`)
      .then(response => {
        if (response.status == 404){
          this.notFound = true;
        } else if (response.status != 200) {
          this.error = true;
        } else {
          this.isResponseAvailable = true;
        }

        return response.json();
      })
      .then(json => {
        if (typeof json != undefined) {
          var data = json.data
          console.log(data)

          this.pag = data.pag
          this.coll = data.colission
          this.overflow = data.overflow

          // switch (data.colision) {
          //   case true:
          //     this.coll = "SIM"
          //     break;
          //   case false:
          //     this.coll = "NÃO"
          //     break;
          // }

          this.access = data.access
        }
      })
    },

    async removeHash() {
      await fetch("http://localhost:3150/hash", {
        method: "DELETE"
      });

      await fetch("http://localhost:3150/hash/initqm")
      .then((response) => {
        return response.json();
      })
      .then((json) => {
        console.log(json)
        this.isInit = json.init;
      });

      this.searchWord = ""
      this.isResponseAvailable = false
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
