---
layout: page
permalink: /teaching/
title: Teaching
description:        A teacher, much like a football coach, must appeal 
                    to the sensibilities of his or her students. He must instill 
                    in them the spirit of achieving the impossible while keeping their 
                    feet firmly grounded in fundamentals. I was fortunate to have been instructed
                     by excellent teachers. My approach to teaching has been inspired by these great 
                     individuals and I hope to pass on the favor to a new generation of
                      chemical engineers.
---

<section id="why">
    <div class="container">

{% for teaching in site.teachings %}
    {% if teaching.status == 'active' %}
    <hr style="width: 100% !important;
                max-width: none!important;
                border:none!important;
                height:1px!important;
                background-color:black;">    
    <div class="row">
        <div class="col-lg-8 col-md-12 text-left">
            <h2><b>{{teaching.course-code}}</b></h2>
            <h3>{{teaching.course-title}}</h3>
            <p>{{teaching.description}}</p>
        </div>
        <div class="col-lg-4 col-md-12 text-left">
            <!-- Uncomment below text when classes have determinedlecture hours and office hours  -->
            <!-- <h3>Lectures:</h3> -->
            <!-- <p> -->
                <!-- {% for day in teaching.days %}
                <p style="padding-left: 1em;">
                    {{ day.key }}
                </p>
                {% endfor %} -->
            <!-- {% if teaching.tutorial %}    
            <h3>Tutorials:</h3>
                <p style="padding-left: 1em;">
                    {{teaching.tutorial}}
                </p>
            {% endif %}     -->
            <!-- </p> -->
            <!-- <h3>Office Hours:</h3> <p style="padding-left: 1em;">{{teaching.office_hours}}</p> -->
            <h3> Course Outline</h3>
            <a href="{{ teaching.course_href | prepend: site.baseurl | prepend: site.url }}" target="_blank">{{teaching.course_out}}</a>
            
          </div>            
    </div>
    {% endif %}
{% endfor %}
    

</div>

</section>
