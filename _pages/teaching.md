---
layout: page
permalink: /teaching/
title: Teaching
description: Innovation does not believe in academic borders. Neither do we! We use insights and methodologies from a variety of scientific and technological domains to meet our objectives.
---

<section id="why">
    <div class="container">
        <div class="row">
            <div class="col-lg-12 text-center">
                <h2 class="section-heading">Teaching</h2>
                <hr class="primary">
                <br />
            </div>
        </div>
    </div>
    <div class="container">

{% for teaching in site.teachings %}
    <div class="row">
        <div class="col-lg-8 col-md-12 text-left">
            <h2><b>{{teaching.course-code}}</b></h2>
            <h3>{{teaching.course-title}}</h3>
            <p>{{teaching.description}}</p>
        </div>
        <div class="col-lg-4 col-md-12 text-left">
            <h3>Lectures</h3>
            <h3>Office Hours</h3>
            <h3>Resources</h3>
        </div>            
    </div>
{% endfor %}
    

</div>

</section>
