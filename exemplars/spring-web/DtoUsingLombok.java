package edu.umass.orgitect.stages_service.dto;

import edu.umass.orgitect.stages_service.entity.Stage;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.ArrayList;
import java.util.Collection;

@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class StageDto {
    private Long id;
    private String action;
    private Long duration;


    public static StageDto fromStage(Stage stage) {
        return StageDto.builder()
                .id(stage.getId())
                .action(stage.getAction())
                .duration(stage.getDuration())
                .build();
    }