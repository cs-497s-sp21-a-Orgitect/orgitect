package edu.umass.orgitect.stages_service.controllers;

import edu.umass.orgitect.stages_service.beans.CollectionResponse;
import edu.umass.orgitect.stages_service.beans.Response;
import edu.umass.orgitect.stages_service.dto.StageDto;
import edu.umass.orgitect.stages_service.service.StageService;
import javassist.NotFoundException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("api/v1/stages")
public class StagesController {

    @Autowired
    StageService stageService;

    @PostMapping(value = "")
    public Response<StageDto> createStage(@RequestBody StageDto stageDto) {
        return new Response<>(stageService.createOne(stageDto));
    }