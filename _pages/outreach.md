---
layout: page
permalink: /outreach/
title: Outreach
description: We are extremely active in the academia community! Here are some of the things we have done!
---



<div class="container">
                    {% for item in site.outreach %}
                    <!-- conference goes here -->
                     <div class="col-md-3 col-lg-3 col-sm-12"  data-toggle="modal" data-target="#myModal">  
                         <img src="{{item.front_image}}" class="img-responsive" alt="{{item.title}}" max-width="100%" >
                         <h3>{{item.title}}</h3>
                         <p>{{item.description}}</p>
                     </div>

                     <!-- Modal -->
                    <div id="myModal" class="modal fade" role="dialog">
                      <div class="modal-dialog">

                        <!-- Modal content-->
                        <div class="modal-content">
                          <div class="modal-header">
                            <button type="button" class="close" data-dismiss="modal">&times;</button>
                            <h4 class="modal-title" style="color: black;">{{item.title}}</h4>
                          </div>
                          <div class="modal-body" style="color: black;">
                            <p>{{item.long_desc}}</p>
                          </div>
                          <div class="modal-footer">
                            <button type="button" class="btn btn-default" data-dismiss="modal" style="color: black;">Close</button>
                          </div>
                        </div>

                      </div>
                    </div>
                    
                    {% endfor %}
                </div>