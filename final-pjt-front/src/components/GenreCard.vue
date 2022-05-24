<template>
  <div class="home container mt-5">
    <h2 class="text-start ms-3" style="color: rgba(240,240,240,1);">Genres</h2>
    <div class="row p-3 g-3">
      <div class="col" @click= "gotoGenre(1)">
        <div class="col-in"></div>
        <div class="genre-name d-flex flex-column justify-content-center ">
          <p> Thriller </p>
        </div>
      </div>
      <div class="col even" @click= "gotoGenre(2)">
        <div class="col-in"></div>
        <div class="genre-name d-flex flex-column justify-content-center ">
            <p> SF / Fantasy </p>
        </div>
      </div>
      <div class="col" @click= "gotoGenre(3)">
        <div class="col-in"></div>
        <div class="genre-name d-flex flex-column justify-content-center ">
            <p> Anime </p>
        </div>
      </div>
      <div class="col even" @click= "gotoGenre(4)">
        <div class="col-in"></div>
        <div class="genre-name d-flex flex-column justify-content-center ">
            <p> Action </p>
        </div>
      </div>
      <div class="col" @click= "gotoGenre(5)">
        <div class="col-in"></div>
        <div class="genre-name d-flex flex-column justify-content-center ">
            <p> Drama </p>
        </div>
      </div>
      <div class="col even" @click= "gotoGenre(6)">
        <div class="col-in"></div>
        <div class="genre-name d-flex flex-column justify-content-center ">
            <p> Documentary </p>
        </div>
      </div>
      <div class="col" @click= "gotoGenre(7)">
        <div class="col-in"></div>
        <div class="genre-name d-flex flex-column justify-content-center ">
            <p> Comedy</p>
        </div>
      </div>
    </div>
    <div class="test"></div>
  </div>
</template>

<script>
export default {
  name: 'GenreCard',
  methods: {
    gotoGenre: function(gid) {
      this.$router.push({name: 'genre', params: { genreId: gid}})
    }
  },
}
</script>

<style>
  .even {
    position: relative;
    top: 20px;
  }
  .col{
  height:400px;
  }
  .col-in:hover{
    opacity:0.5; 
    cursor:pointer;
  }
  .col-in{
    width: 100%;
    height: 100%;
    background:linear-gradient(0deg, rgba(0,0,0,0.5), rgba(100, 100, 100, 0.2)), url('https://www.themoviedb.org/t/p/original/6RuU7NumrO08Bcml5sIgj9zNWFm.jpg');
    overflow: hidden;
  }
  .genre-name{
    position: relative;
    height: 4em;
    bottom: 14em;
    background:linear-gradient(0deg, rgba(0,0,0,0.5), rgba(0, 0, 0, 0.5));
  }
  p {
    font-size: 1.3em;
    margin-bottom: 0;
    color: white;
  }
</style>