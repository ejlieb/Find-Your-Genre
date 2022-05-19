<template>
  <div>
    <div class="for-nav"></div>
    <div class="choose-movie-container container">
      <p id="instruction" >재미있게 봤던, 혹은 보고싶은 영화를 골라주세요!</p>
      <div class="row mt-5">
        <!-- div에 v-for 돌리기 키값으로 title div에 id 줘서 숨겼다 보였다-->
        <div class="poster-card col-2" @mouseover= "showTitle" @mouseout= "hideTitle" id="">
          <img src="https://www.themoviedb.org/t/p/w600_and_h900_bestv2/5HruMN0vvl84AqD7sCDXFNO4RhP.jpg" alt="" class="card-img">
          <div class="card-title d-flex flex-column justify-content-center">
            <p>Title</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ChooseMovie',
  data: function() {
    return {
      
    }
  },
  methods: {
    showTitle: function() {
      
    }
  }
}
</script>

<style>
  #instruction {
    font-size : 2em;
  }
  .choose-movie-container {
    position: relative;
    top: 5em;
  }
  .card-img {
    width: 100%;
  }
  .card-img:hover {
    opacity: 50%;
  }
  .card-title {
    position: relative;
    bottom: 10em;
    max-width: 100%;
  }
</style>