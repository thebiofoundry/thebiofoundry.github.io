---
layout: page
permalink: /Outreach/
title: Outreach
description: 
---
<section id="why">
  <div class="container">
    {% for logo in site.outreach %}
    <div class="media ">
    <div class="col-lg-6 col-md-6 col-sm-12">
      <div class="media-left ">
        <a href="{{logo.link}}" target="_blank"><img src="{{ logo.img | prepend: site.baseurl | prepend: site.url }}" class="media-object"></a>
      </div>
    </div>
    <div class="col-lg-6 col-md-6 col-sm-12">
      <!-- <div class="media-body "> -->
        <!-- <h3 class="media-heading">{{logo.title}}</h3>
        <p>{{logo.description}}</p> -->
      <!-- </div> -->
      </div>
    </div>
    {% endfor %}
   </div>
</section>