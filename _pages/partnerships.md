---
layout: page
permalink: /partnerships/
title: Partnership
description: We collaborate with leaders in the industry to bring the latest technology to the world.
---
<section id="why">
  <div class="container">
    {% for partner in site.partners %}
    <div class="media ">
    <div class="col-lg-4 col-md-4 col-sm-12">
      <div class="media-left ">
        <a href="{{partner.link}}" target="_blank"><img src="{{ partner.img | prepend: site.baseurl | prepend: site.url }}" class="media-object"></a>
      </div>
    </div>
    <div class="col-lg-8 col-md-8 col-sm-12">
      <div class="media-body ">
        <h3 class="media-heading">{{partner.title}}</h3>
        <p>{{partner.description}}</p>
      </div>
      </div>
    </div>
    {% endfor %}
   </div>
</section>