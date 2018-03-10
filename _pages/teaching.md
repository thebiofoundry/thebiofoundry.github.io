---
layout: page
permalink: /teaching/
title: Teaching
description: Innovation does not believe in academic borders. Neither do we! We use insights and methodologies from a variety of scientific and technological domains to meet our objectives.
---

<section id="why">
    <div class="container">

{% for teaching in site.teachings %}
    {% if teaching.status == 'active' %}
    <div class="row">
        <div class="col-lg-8 col-md-12 text-left">
            <h2><b>{{teaching.course-code}}</b></h2>
            <h3>{{teaching.course-title}}</h3>
            <p>{{teaching.description}}</p>
        </div>
        <div class="col-lg-4 col-md-12 text-left">
            <h3>Lectures:</h3>
            <!-- <p> -->
                {% for day in teaching.days %}
                <p style="padding-left: 1em;">
                    {{ day.key }}
                </p>
                {% endfor %}
            <!-- </p> -->
            <h3>Office Hours</h3> <p style="padding-left: 1em;">{{teaching.office_time}}</p>
            <h3>Resources</h3>
        </div>            
    </div>
    {% endif %}
{% endfor %}
    

</div>

</section>
