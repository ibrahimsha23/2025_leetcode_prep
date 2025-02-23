package com.example.urlshortener.service;

import com.example.urlshortener.model.Url;
import com.example.urlshortener.model.UrlDto;
import com.example.urlshortener.repository.UrlRepository;
import com.google.common.hash.Hashing;
import org.apache.commons.lang3.StringUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.nio.charset.StandardCharsets;
import java.time.LocalDate;
import java.time.LocalDateTime;

@Component
public class UrlServiceImp implements UrlService{

    @Autowired
    private UrlRepository urlRepository;

    @Override
    public Url generateShortLink(UrlDto UrlDto) {
        if (StringUtils.isNotEmpty(UrlDto.getUrl())){
            String encodeUrl = encodeUrl(UrlDto.getUrl());
            Url urlToPersist = new Url();
            urlToPersist.setCreationDate(LocalDateTime.now());
            urlToPersist.setOriginalUrl(UrlDto.getUrl());
            urlToPersist.setExpirationDate(getExpirationDate(UrlDto.getExpirationDate(), urlToPersist.getCreationDate()));
            urlToPersist.setShortLink(encodeUrl);
            Url urlToRet = persistShortLink(urlToPersist);
            if (urlToRet != null){
                return urlToRet;
            }
            return null;
        }
        return null;
    }

    private LocalDateTime getExpirationDate(String expirationDate, LocalDateTime creationDate) {
        if(StringUtils.isBlank(expirationDate)){
            return creationDate.plusSeconds(60);
        }
        LocalDateTime expirationDateToRet = LocalDateTime.parse(expirationDate);
        return expirationDateToRet;
    }


    private String encodeUrl(String url) {
        String encodedUrl = "";
        LocalDateTime time = LocalDateTime.now();
        String concatenatedUrl = url + time.toString();
        encodedUrl = Hashing.murmur3_32()
                .hashString(url.concat(time.toString()), StandardCharsets.UTF_8)
                .toString();
        return encodedUrl;
    }

    @Override
    public Url persistShortLink(Url url) {

        Url urlToRet = urlRepository.save(url);
        return urlToRet;
    }

    @Override
    public Url getEncodedUrl(String url) {
        Url urlToRet = urlRepository.findByShortLink(url);
        return urlToRet;

    }

    @Override
    public void deleteShortLink(Url url) {
        urlRepository.delete(url);
    }
}
