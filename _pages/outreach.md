---
layout: page
permalink: /outreach/
title: Outreach
description: Our group is working on a variety of exciting initiatives such as technology entrepreneurship and the organization of technical conferences in some of the hottest areas of science. We are also at the forefront of nucleating Canada’s biotechnology community to catalyze the transformation of the nation’s bioeconomy.
---

<section id="why">
 <div class="container">
    <div class="row">
    {% assign logos = site.outreach | sort: 'weight' %}
    {% for logo in logos %}
    <div class="col-lg-4 col-md-4 col-sm-12">
      <a href="{{logo.link}}" target="_blank"><img src="{{ logo.img | prepend: site.baseurl | prepend: site.url }}" class="outreach-logos"></a>
    </div>
    {% endfor %}
    </div>
   </div>
</section>