<template>
  <div
    id="app"
    class="container"
  >
    <div class="row">
      <div class="col-md-12">
        <h1>Personas</h1>
      </div>
    </div>
    <div class="row">
      <div class="col-md-12">
        <formulario-persona @add-persona="agregarPersona" />
        <tabla-personas
          :personas="personas"
          @delete-persona="eliminarPersona"
          @actualizar-persona="actualizarPersona"
        />
      </div>
    </div>
  <p> Count is {{ store.count }}</p>
  </div>
</template>

<script setup>
import TablaPersonas from '@/components/TablaPersonas.vue'
import FormularioPersona from '@/components/FormularioPersona.vue'
import { ref, onMounted } from 'vue';

defineOptions({
  name: 'app',
});

const personas = ref([]);

const listadoPersonas = async () => {
  // Metodo para obtener un listado de personas
};

const agregarPersona = async (persona) => {
  // Metodo para agregar una persona
};

const eliminarPersona = async (persona_id) => {
  // Metodo para eliminar una persona
};

const actualizarPersona = async (id, personaActualizada) => {
  // Metodo para actualizar una persona
};

// Fetch data when the component is mounted
onMounted(() => {
  listadoPersonas();
});
</script>

<style>
  button {
    background: #009435;
    border: 1px solid #009435;
  }
</style>