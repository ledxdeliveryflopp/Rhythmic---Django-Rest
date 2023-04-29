// Styles
import "@mdi/font/css/materialdesignicons.css";
import "vuetify/styles";

// Vuetify
import { createVuetify } from "vuetify";
import visibilityComponent from "@/ui/VisibilityComponent/index.vue";
import visibilityOffComponent from "@/ui/VisibilityOffComponent/index.vue";
import "material-design-icons-iconfont/dist/material-design-icons.css";
import { aliases, mdi } from "vuetify/iconsets/mdi";

export default createVuetify({
  icons: {
    defaultSet: "mdi",
    aliases,
    sets: {
      mdi,
    },
    values: {
      visibility: {
        component: visibilityComponent,
      },
      visibility_off: {
        component: visibilityOffComponent,
      },
    },
  },
});
