package com.example.urlshortener.controller;

import com.example.urlshortener.model.Url;
import com.example.urlshortener.model.UrlDto;
import com.example.urlshortener.model.UrlErrorResponseDto;
import com.example.urlshortener.model.UrlResponseDto;
import com.example.urlshortener.service.UrlService;
import jakarta.servlet.http.HttpServletResponse;
import org.apache.commons.lang3.StringUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.io.IOException;
import java.time.LocalDateTime;
import java.util.HashMap;
import java.util.Map;

@RestController
public class urlShorteningController {

    @Autowired
    private UrlService urlService;


    @GetMapping("/health")
    public Map<String, Object> healthCheck() {
        Map<String, Object> response = new HashMap<>();
        response.put("status", "UP");
        response.put("timestamp", LocalDateTime.now());
        response.put("message", "Application is running smoothly");
        return response;
    }


    @PostMapping("/generate")
    public ResponseEntity  generateShortLink(@RequestBody UrlDto urlDto){
        Url urltoRet = urlService.generateShortLink(urlDto);
        if (urltoRet != null){
            UrlResponseDto urlResponseDto = new UrlResponseDto();
            urlResponseDto.setOriginalUrl(urltoRet.getOriginalUrl());
            urlResponseDto.setExpirationDate(urltoRet.getExpirationDate());
            urlResponseDto.setShortLink(urltoRet.getShortLink());
            return new ResponseEntity<UrlResponseDto>(urlResponseDto, HttpStatus.OK);
        }

        UrlErrorResponseDto urlErrorResponseDto = new UrlErrorResponseDto();
        urlErrorResponseDto.setStatus("404");
        urlErrorResponseDto.setError("There is an error processing your request, please try again");
        return new ResponseEntity<UrlErrorResponseDto>(urlErrorResponseDto, HttpStatus.FORBIDDEN);
    }

    @GetMapping("/{shortLink}")
    public ResponseEntity redirectToOriginalUrl(@PathVariable String shortLink, HttpServletResponse response) throws IOException {
        if (StringUtils.isEmpty(shortLink)){
            UrlErrorResponseDto urlErrorResponseDto = new UrlErrorResponseDto();
            urlErrorResponseDto.setStatus("404");
            urlErrorResponseDto.setError("INVALID URL");
            return new ResponseEntity<UrlErrorResponseDto>(urlErrorResponseDto, HttpStatus.FORBIDDEN);
        }

        Url urlToRet = urlService.getEncodedUrl(shortLink);

        if (urlToRet == null){
            UrlErrorResponseDto urlErrorResponseDto = new UrlErrorResponseDto();
            urlErrorResponseDto.setStatus("200");
            urlErrorResponseDto.setError("URL MIGHT EXPIRED, please try generating on");
            return new ResponseEntity<UrlErrorResponseDto>(urlErrorResponseDto, HttpStatus.FORBIDDEN);
        }

//        if(urlToRet.getExpirationDate().isBefore(LocalDateTime.now()))
//        {
//            urlService.deleteShortLink(urlToRet);
//            UrlErrorResponseDto urlErrorResponseDto = new UrlErrorResponseDto();
//            urlErrorResponseDto.setError("Url Expired. Please try generating a fresh one.");
//            urlErrorResponseDto.setStatus("200");
//            return new ResponseEntity<UrlErrorResponseDto>(urlErrorResponseDto,HttpStatus.OK);
//        }

        response.sendRedirect(urlToRet.getOriginalUrl());;
        return null;

    }
}
